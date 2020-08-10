ms<-read.csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/full_reg_panel.csv')
hs<-read.csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/VAM_reg/balanced_panel_real_hs.csv')
ms$var <-5
hs$var <-5

library(ggplot2)
library(RColorBrewer)
library(ggpubr)



a<-ggplot(ms,aes(var,dist_total_val_per_pupil)) +scale_y_continuous(breaks = seq(0, 2500000, by = 250000)) + geom_boxplot(aes(colour = Description), outlier.colour = "black", outlier.shape = 1)+ 
  scale_color_brewer(palette="Dark2") +
   theme(aspect.ratio=1, axis.title.x=element_blank(), 
        plot.background = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position = "none",
        axis.text.x=element_blank(), axis.ticks.x=element_blank()) +labs(y = 'District Wealth $ per Pupil (Primary Schools)')

b<-ggplot(hs,aes(var,dist_total_val_per_pupil)) +scale_y_continuous(breaks = seq(0, 2500000, by = 250000)) + geom_boxplot(aes(colour = Description), outlier.colour = "black", outlier.shape = 1)+ 
  scale_color_brewer(palette="Dark2") +
  theme(aspect.ratio=1, axis.title.x=element_blank(), 
        plot.background = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.position = "none",
        axis.text.x=element_blank(), axis.ticks.x=element_blank()) +labs(y = 'District Wealth $ per Pupil (High Schools)')

ggarrange(a, b, nrow = 2)
