function [pdf_EV, pdf_var, pdf_Spearman, pdf_Sch_Wolf] = Num_pdf_Summary(theta_min,theta_max,grain,Num_pdf,fig)
%This function takes in the minimal and maximal parameter values, the
%[grain] and [Num_pdf] numerical pdf surface to generate (a) mean, (b) variance, 
% (c) association, (d) dependence, and (e) plots. Written by Stephen Broomell 5/16/2023.
%Inputs
%   [theta_min] = column vector of the minimal parameter values for [model]
%   [theta_min] = column vector of the maximal parameter values for [model]
%   [grain] = resolution of sampling distribution
%   [Num_pdf] = Matrix of numerically computed probability for each
%   parameter value
%   [fig] = 1 generates marginal bivariate plots; 0 suppresses plots.
%Outputs
%   [pdf_EV] = expected value of each parameter in [Num_pdf].
%   [pdf_var] = variance of each parameter in [Num_pdf].   
%   [pdf_Spearman] = association between each parameter in [Num_pdf].
%   [pdf_Sch_Wolf] = dependence between each parameter in [Num_pdf].

%Generate Grid Values for Parameters
Theta_1 = cell2mat(arrayfun(@(x_min,x_max) linspace(x_min,x_max,grain),theta_min,theta_max,'UniformOutput',false));

%Create Empirical Pdf
A = size(Num_pdf);
%2 parameter - Bivariate Distribution
if length(A) == 2
    
    %Compute Marginals
    Marg1 = sum(Num_pdf,2);
    Marg2 = sum(Num_pdf,1);

    %Compute Expected Value;
    EV_p1 = sum(Marg1'.*Theta_1(1,:));
    EV_p2 = sum(Marg2.*Theta_1(2,:));

    pdf_EV = [EV_p1 EV_p2];

    %Compute Variance
    VAR_p1 = sum(Marg1'.*(Theta_1(1,:) - EV_p1).^2);
    VAR_p2 = sum(Marg2.*(Theta_1(2,:) -EV_p2).^2);    

    pdf_var = [VAR_p1 VAR_p2];

    %Compute Association and Dependence Estiamtes
    [Sp_1_2,SW_1_2] = Numerical_Copula_Analysis_V2(Num_pdf);

    pdf_Spearman = [1 Sp_1_2 ;
                    Sp_1_2 1 ];
    pdf_Sch_Wolf = [1 SW_1_2 ;
                    SW_1_2 1 ];

    %Create Figure
    if fig == 1
        figure;
        subplot(2,2,1); plot(Theta_1(1,:),sum(Num_pdf,2));
        xlabel('Parameter 1');
        ylabel('Probability');

        [X,Y] = meshgrid(Theta_1(2,:),Theta_1(1,:));
        subplot(2,2,3); h = pcolor(Y,X,Num_pdf);
        set(h, 'EdgeColor', 'none');
        xlabel('Parameter 1');
        ylabel('Parameter 2');

        subplot(2,2,4); plot(Theta_1(2,:),sum(Num_pdf,1));
        xlabel('Parameter 2');
        ylabel('Probability');
    end

%3 parameter
elseif length(A) == 3

    %Bivariate Marginal representations
    Bivar_1_2 = squeeze(sum(Num_pdf,3));
    Bivar_1_3 = squeeze(sum(Num_pdf,2));
    Bivar_2_3 = squeeze(sum(Num_pdf,1));

    %Marginals
    Marg1 = sum(Bivar_1_2,2);
    Marg2 = sum(Bivar_1_2,1);
    Marg3 = sum(Bivar_1_3,1);

    %Compute Expected Value;
    EV_p1 = sum(Marg1'.*Theta_1(1,:));
    EV_p2 = sum(Marg2.*Theta_1(2,:));
    EV_p3 = sum(Marg3.*Theta_1(3,:));

    pdf_EV = [EV_p1 EV_p2 EV_p3];

    %Compute Variance
    VAR_p1 = sum(Marg1'.*(Theta_1(1,:) - EV_p1).^2);
    VAR_p2 = sum(Marg2.*(Theta_1(2,:) - EV_p2).^2);
    VAR_p3 = sum(Marg3.*(Theta_1(3,:) - EV_p3).^2);

    pdf_var = [VAR_p1 VAR_p2 VAR_p3];

    %Compute Association and Dependence Estiamtes
    [Sp_1_2,SW_1_2] = Numerical_Copula_Analysis_V2(Bivar_1_2);
    [Sp_1_3,SW_1_3] = Numerical_Copula_Analysis_V2(Bivar_1_3);
    [Sp_2_3,SW_2_3] = Numerical_Copula_Analysis_V2(Bivar_2_3);

    pdf_Spearman = [1 Sp_1_2 Sp_1_3 ;
                    Sp_1_2 1 Sp_2_3 ;
                    Sp_1_3 Sp_2_3 1 ];
    pdf_Sch_Wolf = [1 SW_1_2 SW_1_3 ;
                    SW_1_2 1 SW_2_3 ;
                    SW_1_3 SW_2_3 1 ];

    %Create Figure
    if fig == 1
        %Create Figure
        figure;
        subplot(3,3,1); plot(Theta_1(1,:),sum(Bivar_1_2,2));
        xlabel('Parameter 1');
        ylabel('Probability');

        [X,Y] = meshgrid(Theta_1(2,:),Theta_1(1,:));
        subplot(3,3,4); h = pcolor(Y,X,Bivar_1_2);
        set(h, 'EdgeColor', 'none');
        xlabel('Parameter 1');
        ylabel('Parameter 2');

        subplot(3,3,5); plot(Theta_1(2,:),sum(Bivar_1_2,1));
        xlabel('Parameter 2');
        ylabel('Probability');

        [X,Y] = meshgrid(Theta_1(3,:),Theta_1(1,:));
        subplot(3,3,7); h = pcolor(Y,X,Bivar_1_3);
        set(h, 'EdgeColor', 'none');
        xlabel('Parameter 1');
        ylabel('Parameter 3');

        [X,Y] = meshgrid(Theta_1(3,:),Theta_1(2,:));
        subplot(3,3,8); h = pcolor(Y,X,Bivar_2_3);
        set(h, 'EdgeColor', 'none');
        xlabel('Parameter 2');
        ylabel('Parameter 3');

        subplot(3,3,9); plot(Theta_1(3,:),sum(Bivar_1_3,1));
        xlabel('Parameter 3');
        ylabel('Probability');
    end

%4 parameter
elseif length(A) == 4

    %Bivariate Marginal representations
    Bivar_1_2 = squeeze(sum(sum(Num_pdf,3),4));
    Bivar_1_3 = squeeze(sum(sum(Num_pdf,2),4));
    Bivar_2_3 = squeeze(sum(sum(Num_pdf,1),4));
    Bivar_1_4 = squeeze(sum(sum(Num_pdf,2),3));
    Bivar_2_4 = squeeze(sum(sum(Num_pdf,1),3));
    Bivar_3_4 = squeeze(sum(sum(Num_pdf,1),2));

    %Marginals
    Marg1 = sum(Bivar_1_2,2);
    Marg2 = sum(Bivar_1_2,1);
    Marg3 = sum(Bivar_1_3,1);
    Marg4 = sum(Bivar_1_4,1);    

    %Compute Expected Value;
    EV_p1 = sum(Marg1'.*Theta_1(1,:));
    EV_p2 = sum(Marg2.*Theta_1(2,:));
    EV_p3 = sum(Marg3.*Theta_1(3,:));
    EV_p4 = sum(Marg4.*Theta_1(4,:));

    pdf_EV = [EV_p1 EV_p2 EV_p3 EV_p4];

    %Compute Variance
    VAR_p1 = sum(Marg1'.*(Theta_1(1,:) - EV_p1).^2);
    VAR_p2 = sum(Marg2.*(Theta_1(2,:) - EV_p2).^2);
    VAR_p3 = sum(Marg3.*(Theta_1(3,:) - EV_p3).^2);
    VAR_p4 = sum(Marg4.*(Theta_1(4,:) - EV_p4).^2);

    pdf_var = [VAR_p1 VAR_p2 VAR_p3 VAR_p4];

    %Compute Association and Dependence Estiamtes
    [Sp_1_2,SW_1_2] = Numerical_Copula_Analysis_V2(Bivar_1_2);
    [Sp_1_3,SW_1_3] = Numerical_Copula_Analysis_V2(Bivar_1_3);
    [Sp_2_3,SW_2_3] = Numerical_Copula_Analysis_V2(Bivar_2_3);
    [Sp_1_4,SW_1_4] = Numerical_Copula_Analysis_V2(Bivar_1_4);
    [Sp_2_4,SW_2_4] = Numerical_Copula_Analysis_V2(Bivar_2_4);
    [Sp_3_4,SW_3_4] = Numerical_Copula_Analysis_V2(Bivar_3_4);

    pdf_Spearman = [1 Sp_1_2 Sp_1_3 Sp_1_4;
                    Sp_1_2 1 Sp_2_3 Sp_2_4;
                    Sp_1_3 Sp_2_3 1 Sp_3_4;
                    Sp_1_4 Sp_2_4 Sp_3_4 1];
    pdf_Sch_Wolf = [1 SW_1_2 SW_1_3 SW_1_4;
                    SW_1_2 1 SW_2_3 SW_2_4;
                    SW_1_3 SW_2_3 1 SW_3_4;
                    SW_1_4 SW_2_4 SW_3_4 1];

    %Create Figure
    figure;
    subplot(4,4,1); plot(Theta_1(1,:),sum(Bivar_1_2,2));
    xlabel('Parameter 1');
    ylabel('Probability');

    [X,Y] = meshgrid(Theta_1(2,:),Theta_1(1,:));
    subplot(4,4,5); h = pcolor(Y,X,Bivar_1_2);
    set(h, 'EdgeColor', 'none');
    xlabel('Parameter 1');
    ylabel('Parameter 2');

    subplot(4,4,6); plot(Theta_1(2,:),sum(Bivar_1_2,1));
    xlabel('Parameter 2');
    ylabel('Probability');

    [X,Y] = meshgrid(Theta_1(3,:),Theta_1(1,:));
    subplot(4,4,9); h = pcolor(Y,X,Bivar_1_3);
    set(h, 'EdgeColor', 'none');
    xlabel('Parameter 1');
    ylabel('Parameter 3');

    [X,Y] = meshgrid(Theta_1(3,:),Theta_1(2,:));
    subplot(4,4,10); h = pcolor(Y,X,Bivar_2_3);
    set(h, 'EdgeColor', 'none');
    xlabel('Parameter 2');
    ylabel('Parameter 3');

    subplot(4,4,11); plot(Theta_1(3,:),sum(Bivar_1_3,1));
    xlabel('Parameter 3');
    ylabel('Probability');

    [X,Y] = meshgrid(Theta_1(4,:),Theta_1(1,:));
    subplot(4,4,13); h = pcolor(Y,X,Bivar_1_4);
    set(h, 'EdgeColor', 'none');
    xlabel('Parameter 1');
    ylabel('Parameter 4');

    [X,Y] = meshgrid(Theta_1(4,:),Theta_1(2,:));
    subplot(4,4,14); h = pcolor(Y,X,Bivar_2_4);
    set(h, 'EdgeColor', 'none');
    xlabel('Parameter 2');
    ylabel('Parameter 4');

    [X,Y] = meshgrid(Theta_1(4,:),Theta_1(3,:));
    subplot(4,4,15); h = pcolor(Y,X,Bivar_3_4);
    set(h, 'EdgeColor', 'none');
    xlabel('Parameter 3');
    ylabel('Parameter 4');

    subplot(4,4,16); plot(Theta_1(4,:),sum(Bivar_1_4,1));
    xlabel('Parameter 4');
    ylabel('Probability');
end

end%of Num_pdf_Summary.m

%%%%%%%%%%%%%%%%%%%%%%%%% Subroutines %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [Spearman,Sch_Wolff] = Numerical_Copula_Analysis_V2(pdf)

%   Detailed explanation goes here
[r,c] = size(pdf);
%Compute Cumulative Distribution and Marginals
cdf_1 = (cumsum(cumsum(pdf,1),2));               %Compute Numerical Sums
cdf = [0, zeros(1,c); zeros(r,1) cdf_1]; %Make Sure CDF starts at zero

%Compute Marginal CDF for each parameter
F1 = cdf(:,end)';
F2 = cdf(end,:);

%Uniform Scale base on CDF Marginals
u = [F1];
v = [F2];

%Create Independence Copula
C_PI = u'*v;
%M = 
[Xv,Yu] = meshgrid(v,u); %Create 3D Versions of u and v

%Compute Maximum Approximate Value
M_mat(:,:,1) = Xv;
M_mat(:,:,2) = Yu;
M = min(M_mat,[],3);
[~,ub1] = convhull(Xv,Yu,M-C_PI);
ub1 = ub1;

%Compute Minimum Approximate Value
M_mat(:,:,1) = Xv+Yu-1;
M_mat(:,:,2) = zeros(size(Yu));
W = max(M_mat,[],3);
[~,lb1] = convhull(Xv,Yu,W-C_PI);
lb1 = lb1;

%Compute Signed Volume between surfaces
Hull_Sign = (cdf > C_PI);                     %Indicates Positive Values
Pos_Part = cdf.*Hull_Sign - C_PI.*Hull_Sign;  %Compute difference only for positive

Neg_Part = cdf.*~Hull_Sign - C_PI.*~Hull_Sign;%Compute difference only for negative

%Numercially estimate the volume of the convex hull of positive and negative
%parts separately
if var(var(Pos_Part)) == 0  %Coplanar points result in error from convhull.m, but should be 0
    Pos_V = 0;
else
    [~,Pos_V] = convhull(Xv,Yu,Pos_Part);
end
if var(var(Neg_Part)) == 0 %Coplanar points result in error from convhull.m, but should be 0
    Neg_V = 0;
else
    [~,Neg_V] = convhull(Xv,Yu,Neg_Part);
end
%Rescale based on maximum and minimum copulas to correct for approximate calculations
Pos_V = ((Pos_V))./(ub1);
Neg_V = ((Neg_V))./(lb1);

%Compute Non-parametric measures of association and dependence
Spearman = (Pos_V - Neg_V);    %Spearman rho - association
Sch_Wolff = (Pos_V + Neg_V);    %Sch_Wolff sigma - dependence
end%of Numerical_Copula_Analysis_V2
