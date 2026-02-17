function [KL_pdf] = KL_Samp_Binom_paramSplit(model,X,theta_0,theta_min,theta_max,grain)
%This function takes in the name of an m-file that takes in stimuli [x] and
%parameters [theta] to produce a binomial prediction. Written by Stephen
%Broomell 5/16/2023.
%   [model] = string of the function name for the model
%   [X] = Definition of experimental stimuli
%   [theta_0] = focal parameter values;
%   [theta_min] = column vector of the minimal parameter values for [model]
%   [theta_min] = column vector of the maximal parameter values for [model]
%   [grain] = resolution of sampling distribution
%Outputs
%   [KL_pdf] = numerical sampling distribution.

%Generate Grid Values for Parameters
Theta_1 = cell2mat(arrayfun(@(x_min,x_max) linspace(x_min,x_max,grain),theta_min,theta_max,'UniformOutput',false));
%[Theta_1] is a matrix where each row is a parameter in theta and the columns
%represent parameter values.

paramN = size(Theta_1,1);

%%%%%%%%%%%%%%%%% - 4 Parameter - %%%%%%%%%%%%%%%%%%%%%%%
%elseif paramN == 4
    KL_exp_adj = zeros(grain,grain,grain,grain);
    T1 = Theta_1(1,:);
    T2 = Theta_1(2,:);
    T3 = Theta_1(3,:);
    T4 = Theta_1(4,:);   
    parfor i = 1:grain
        for j = 1:grain
            for k = 1:grain
                for l = 1:grain
                    KL_exp_adj(i,j,k,l) = KL_fun_split(theta_0,[T1(i) T2(j) T3(k) T4(l)],model,X);
                end
            end
        end
    end
    KL_pdf = KL_exp_adj/sum(KL_exp_adj,'all',"omitnan");
%end 

end %of KL_Samp_Binom_V1

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [KL_exp_adj] = KL_fun_split(theta_0,theta_1,model,X)

%Turn model string input into a function handle
name = strcat('@',model);
modelFun = eval(name);

%Part 1

Pi_of_G1_0 = modelFun(theta_0([1 2 3]),X);
Pi_of_G1_1 = modelFun(theta_1([1 2 3]),X);

%Compute KL Divergence
KL_vect = Pi_of_G1_0.*log(Pi_of_G1_0./Pi_of_G1_1) + (1-Pi_of_G1_0).*log((1-Pi_of_G1_0)./(1-Pi_of_G1_1));

KL_exp = exp(-1*KL_vect);

%Compute Correction Term
sig_0 = Pi_of_G1_0.*(1-Pi_of_G1_0);
sig_1 = Pi_of_G1_1.*(1-Pi_of_G1_1);

sig_fun_1_v = (sqrt(sig_1)./sqrt(sig_0)).^(-1.*(sig_1./sig_0));
sig_fun_2_v = exp( (sig_1.^2 - sig_0.^2)./((4.*sig_0.^2)) );

Correction = (sig_fun_1_v.*sig_fun_2_v);

%As the variance [sig] gets extreme, the numerical computation of the correction
% becomes unstable. Also, the effect of the correction here is minimal. 
% This code reduces the effect of the correction for high sigma
Index = (abs(.5-Pi_of_G1_1) >= .4 | abs(.5-Pi_of_G1_0) >= .4);
Correction(Index) = ((sig_fun_1_v(Index).*sig_fun_2_v(Index)) + 1)/2;

% This code eliminates the correction for extreme Sigma
Index = (abs(.5-Pi_of_G1_1) >= .49 | abs(.5-Pi_of_G1_0) >= .49);
Correction(Index) = 1;

KL_Corrected_1 = KL_exp./(Correction);  %Apply Correction

%Part 2

Pi_of_G1_0 = modelFun(theta_0([1 2 4]),X);
Pi_of_G1_1 = modelFun(theta_1([1 2 4]),X);

%Compute KL Divergence
KL_vect = Pi_of_G1_0.*log(Pi_of_G1_0./Pi_of_G1_1) + (1-Pi_of_G1_0).*log((1-Pi_of_G1_0)./(1-Pi_of_G1_1));

KL_exp = exp(-1*KL_vect);

%Compute Correction Term
sig_0 = Pi_of_G1_0.*(1-Pi_of_G1_0);
sig_1 = Pi_of_G1_1.*(1-Pi_of_G1_1);

sig_fun_1_v = (sqrt(sig_1)./sqrt(sig_0)).^(-1.*(sig_1./sig_0));
sig_fun_2_v = exp( (sig_1.^2 - sig_0.^2)./((4.*sig_0.^2)) );

Correction = (sig_fun_1_v.*sig_fun_2_v);

%As the variance [sig] gets extreme, the numerical computation of the correction
% becomes unstable. Also, the effect of the correction here is minimal. 
% This code reduces the effect of the correction for high sigma
Index = (abs(.5-Pi_of_G1_1) >= .4 | abs(.5-Pi_of_G1_0) >= .4);
Correction(Index) = ((sig_fun_1_v(Index).*sig_fun_2_v(Index)) + 1)/2;

% This code eliminates the correction for extreme Sigma
Index = (abs(.5-Pi_of_G1_1) >= .49 | abs(.5-Pi_of_G1_0) >= .49);
Correction(Index) = 1;

KL_Corrected_2 = KL_exp./(Correction);  %Apply Correction

KL_exp_adj = prod(KL_Corrected_1)*prod(KL_Corrected_2);      %Compute Final Corrected exp(KL) value as product across trials.

end % of KL_fun.m
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%