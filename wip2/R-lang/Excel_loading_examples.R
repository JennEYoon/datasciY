# Script to read Excel format file into R.
# by Jennifer Yoon
# Date: 9/12/2016
#
#  Install xlsx package if not already installed in R.
#  install.packages("xlsx", dependencies = TRUE)
#
#  Load package into R Library
require(xlsx)
library(xlsx)

# Replace filename, sheetName with your own inputs prior to running.
dat <- read.xlsx("whiteWineQuality.xlsx", sheetName = "Sheet1")
#  Has rowIndex, colINdex functions.
#  Use read.xlsx2 package for faster read on big data.