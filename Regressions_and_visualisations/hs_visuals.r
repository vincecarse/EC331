hs<-read.csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel_real_hs.csv')

library(ggplot2)
library(RColorBrewer)
library(ggpubr)


a<-ggplot(hs,aes(TAKS_math_gr10,TAKS_math_gr9, color = Year))+geom_point()+   theme(aspect.ratio=1)

b<-ggplot(hs,aes(TAKS_ELA_gr10,TAKS_reading_gr9, color = Year))+geom_point()+   theme(aspect.ratio=1)

c<-ggplot(hs,aes(TAKS_math_gr10,TAKS_math_gr9, color = Description))+geom_point()+scale_color_brewer(palette="Dark2") +
  stat_smooth(method = lm)+ theme(aspect.ratio=1)

d<-ggplot(hs,aes(TAKS_ELA_gr10,TAKS_reading_gr9, color = Description))+geom_point()+scale_color_brewer(palette="Dark2") +
  stat_smooth(method = lm)+ theme(aspect.ratio=1)

ggarrange(a, b, nrow=2, common.legend = TRUE, legend = 'bottom')



ggarrange(c, d, nrow=2, common.legend = TRUE, legend = 'bottom')




e<- ggplot(hs,aes(TAKS_part))+geom_histogram(colour = 'white', fill = 'salmon')+ theme(aspect.ratio=1)+labs(y = 'Count(High Schools)')

f<- ggplot(ms,aes(TAKS_part))+geom_histogram(colour = 'white', fill = 'salmon')+ theme(aspect.ratio=1)+labs(y = 'Count(Elementary Schools)')

ggarrange(e, f, ncol=2, common.legend = TRUE, legend = 'bottom')
