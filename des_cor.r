# Importing file
full_vars <- read.table("qsarvars.txt", header=TRUE, sep="\t", dec=".")

# Getting coorelation to U and V
v_vals <- as.vector(full_vars['U'])
u_vals <- as.vector(full_vars['V'])

headers <- colnames(full_vars)[3:125]

v_cors <- list()
u_cors <- list()

rsq <- function (x, y) {cor(x, y)^2}

for (item in headers) {
  desc <- as.vector(full_vars[item])
  vr <- rsq(v_cors,uf)
  ur <- rsq(u_cors, vf)
  append(v_cors, vr)
  append(u_cors, ur)
}
