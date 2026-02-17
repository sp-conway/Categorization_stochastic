function [pi_of_A] = GCM_3p(params,X)
%w is the weight on the position attribute
%c is the generalization parameter
%d_._H is the difference in stimulus height
%d_._P is the difference in stimulus position

d_A_H = X(:,[1:4]);
d_B_H = X(:,[5:8]);
d_A_P = X(:,[9:12]);
d_B_P = X(:,[13:16]);

w = params(1);
c = params(2);
theta = params(3);
b = .5;

d_A = w.*d_A_P - (1-w).*d_A_H;
d_B = w.*d_B_P - (1-w).*d_B_H;
s_A = sum(exp(-1.*c.*d_A),2);
s_B = sum(exp(-1.*c.*d_B),2);

pi_of_A = ( b.*(s_A.^theta) ) ./ ( b.*(s_A.^theta) + (1-b).*(s_B.^theta)  );

end