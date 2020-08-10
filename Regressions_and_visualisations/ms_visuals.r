ms<-read.csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/full_reg_panel.csv')

library(ggplot2)
library(RColorBrewer)
library(ggpubr)

a<-ggplot(ms,aes(TAKS_math_gr5,TAKS_math_gr4, colour = Year))+geom_point()+ theme(aspect.ratio=1) +
  theme(legend.position = "none")
###+ scale_color_gradient2(low="blue",mid = "white",high="red")

b<-ggplot(ms,aes(TAKS_reading_gr5,TAKS_reading_gr4, colour = Year))+geom_point() +
 theme(legend.position = "none")+ theme(aspect.ratio=1)

c<-ggplot(ms,aes(TAKS_math_gr5,TAKS_math_gr4, colour = Description))+geom_point()+scale_color_brewer(palette="Dark2") +
 theme(legend.position = "none") +stat_smooth(method = lm)+ theme(aspect.ratio=1)

d<-ggplot(ms,aes(TAKS_reading_gr5,TAKS_reading_gr4, colour = Description))+geom_point()+scale_color_brewer(palette="Dark2") +
  theme(legend.position = "none") +stat_smooth(method = lm)+ theme(aspect.ratio=1)

ggarrange(a, b, c, d, nrow = 2, ncol =2)
          
ms$var <- 5

colnames(ms)

ggplot(ms,aes(var,dist_total_val_per_pupil)) + geom_boxplot(aes(colour = Description), outlier.colour = "black", outlier.shape = 1)+ 
  theme(aspect.ratio=1, axis.title.x=element_blank(), 
        plot.background = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.text.x=element_blank(), axis.ticks.x=element_blank()) +labs(y = 'District Wealth per Pupil')
        

colnames(ms)