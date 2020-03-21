df <- read.csv('/Users/vincentcarse/Desktop/Thesis/Texas_Education/Regression/reg_data.csv')
reg <- lm(CA08AMA1S17R~CA06AMA1S17R+CA07AMA1S17R+teacher_spend+students, data=df)


cols <- c('CA06AMA1S17R', 'CA07AMA1S17R', 'teacher_spend', 'students')




#
