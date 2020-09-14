library(readxl)
library(ggplot2)
library(reshape2)
library(showtext)

showtext_auto()

# reading raw data
File <- commandArgs(trailingOnly = TRUE)[1]

A <- read_excel(File, col_names = F)

# Data Clean
A <- unique(A)

colnames(A)[11] <- "Primer"
colnames(A)[21] <- "Result"
colnames(A)[26] <- "Plate"
A$Guest <- paste(A[[5]],A[[8]],sep="_")

# Na replace
NA_0 <- function(B){
  if(is.na(B)==TRUE){
    B = 0
  }
  return(B)
}

# Whole Result
## Success Rate
Suc_plot <- function(A,OUTPUT){
  N_Suc <- length(which(A$Result== "报告成功"))
  N_Fail <- length(which(A$Result== "报告失败"))
  Rate = N_Suc/(N_Suc+N_Fail)
  Rate = paste("总成功率: ",round(Rate*100, 2),"%", sep="")
  UP = 0.1*N_Fail
  ggplot(A) + geom_bar(aes(x=A$Result), fill="steelblue")+ theme_light()+
    geom_text(aes(x=1,y=1.1*N_Suc),label=Rate)+
    geom_text(aes(x="报告成功",y=UP+N_Suc,label=N_Suc))+
    geom_text(aes(x="报告失败",y=UP+N_Fail,label=N_Fail))
  ggsave(OUTPUT)
}

## Guest Plot
Guest_Count <- function(A,OUTPUT){
  Order = rownames(sort(table(A$Guest),decreasing = F))
  A$Guest <- factor(A$Guest, levels=Order)
  ggplot(A)+geom_bar(aes(x=A$Guest, fill=A$Result)) +
      theme_light() + theme(axis.text.x = element_text(hjust = 1))+
      coord_flip()
  ggsave(OUTPUT, w= 7,h=12)
}

Guest_Suc <- function(A,OUT1,OUT2){
  G_list <- unique(A$Guest)
  # Statistic
  Result = data.frame()
    for(i in G_list){
      Fail = table(A$Result[which(A$Guest==i)])['报告失败'][[1]]
      Suc  = table(A$Result[which(A$Guest==i)])['报告成功'][[1]]
      Fail = NA_0(Fail)
      Suc  = NA_0(Suc)
      Num  = Fail + Suc
      Rate  = Fail/Num
      tmp = data.frame(ID = i, Num = Num, Fail = Rate)
      Result = rbind(Result, tmp)
    }
  # Order and plot
  Order = Result$ID[order(Result$Fail, decreasing = F)]
  A$Guest <- factor(A$Guest, levels=Order)
  ggplot(A)+geom_bar(aes(x=A$Guest, fill=A$Result)) +
      theme_light() + theme(axis.text.x = element_text(hjust = 1))+
      coord_flip()
  ggsave(OUT1, w= 7,h=12)
  ggplot(A)+geom_bar(aes(x=A$Guest, fill=A$Result), position = 'fill') +
      theme_light() + theme(axis.text.x = element_text(hjust = 1))+
      coord_flip()+
      geom_text(data=Result, aes(x=Result$ID, y= 0.5, label=Result$Num))
  ggsave(OUT2, w= 7,h=12)
}

Primer_Suc <- function(A,OUT1,OUT2){
  P_list <- unique(toupper(A$Primer))
  # Statistic
  Result = data.frame()
  for(i in P_list){
    Fail = table(A$Result[which(toupper(A$Primer)==i)])['报告失败'][[1]]
    Suc  = table(A$Result[which(toupper(A$Primer)==i)])['报告成功'][[1]]
    Fail = NA_0(Fail)
    Suc  = NA_0(Suc)
    Num  = Fail + Suc
    Rate  = Fail/Num
    tmp = data.frame(ID = i, Num = Num, Fail = Rate)
    Result = rbind(Result, tmp)
  }
  # Order and plot
  Order = Result$ID[order(Result$Fail, decreasing = F)]
  A$Primer <- factor(toupper(A$Primer), levels=Order)
  ggplot(A)+geom_bar(aes(x=A$Primer, fill=A$Result)) +
      theme_light() + theme(axis.text.x = element_text(hjust = 1))+
      coord_flip()
  ggsave(OUT1, w= 7,h=12)
  ggplot(A)+geom_bar(aes(x=A$Primer, fill=A$Result), position = 'fill') +
      theme_light() + theme(axis.text.x = element_text(hjust = 1))+
      coord_flip()+
      geom_text(data=Result, aes(x=Result$ID, y= 0.5, label=Result$Num))
  ggsave(OUT2, w= 7,h=12)
}

main <- function(A,pre){
  Suc_plot(A, paste(pre,"1_Success.png",sep="_"))
  Guest_Count(A, paste(pre,"2_Guest.png",sep="_"))
  Guest_Suc(A,paste(pre,"3_Gue_rate1.png",sep="_"),paste(pre,"Gue_rate2.png",sep="_"))
  Primer_Suc(A,paste(pre,"4_Pri_rate1.png",sep="_"),paste(pre,"Pri_rate2.png",sep="_"))
}
# latest Plates
P_list <- unique(toupper(sort(A$Plate, decreasing = T)))

## Latest 1
B = A[toupper(A$Plate) %in% P_list[1],]
main(B,'Latest1')

## Latest 2
B = A[toupper(A$Plate) %in% P_list[1:2],]
main(B,'Latest2')


## Latest 5
B = A[toupper(A$Plate) %in% P_list[1:5],]
main(B,'Latest5')

## Latest 10
B = A[toupper(A$Plate) %in% P_list[1:5],]
main(B,'Latest10')


## Latest 20
B = A[toupper(A$Plate) %in% P_list[1:5],]
main(B,'Latest20')
