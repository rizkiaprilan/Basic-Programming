#TUTORIAL BAHASA R
#CTRL + ALT Untuk menjalankan per Line

getwd()  #working directorynya
setwd("C:/Users/riski/OneDrive/Documents/My Documents/Telkom - Big Data Management/Belajar/R")   #set working directorynya

A<-matrix(c(1,2,3,4,5,6),nrow = 3,ncol = 2)  #membuat data dalam bentuk matrix
A
B<-matrix(c(2,4,6,8),nrow = 2,ncol = 2)  #membuat data dalam bentuk matrix
B
D<-cbind(A,B)  #variabel D akan menggabungkan A dan B dengan row yang sama
D
E<-rbind(A,B)  #variabel D akan menggabungkan A dan B dengan col yang sama
E
mylist<-list(A,B)  #list yang menampilkan seluruh matrix
mylist

help(c)   #mencari tau command c
?c
help.search("probability")  
help.start()  #dasar dari R
