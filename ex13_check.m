clc
clear all
close all

syms m
syms t

A = [0 1/2 1/2;
    0 0 1/2;
    1 1/2 0];

n = size(A, 1)
S = 1/n*ones(n,n)

M = (1-m)*A+m*S
D = M-eye(3)*(m-1)/2
rank(D)
rref(D)
[x, eigs] = eig(M)