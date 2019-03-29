#!/bin/bash

#chmod +x main.sh
#./main.sh

python main.py

gnuplot <<- EOF
  set grid layerdefault linewidth 1
  set xlabel "Passo"
  set ylabel "Yn"
  set title "Metodo numerico de  Euler"
  set style line 1 pt 1
  set style line 2 pt 2
  set term png
  set output "graphs/euler.png"
  plot "output/euler.csv" u 1:2 pt 1 title "Euler" w linespoints
EOF

gnuplot <<- EOF
  set grid layerdefault linewidth 1
  set xlabel "Passo"
  set ylabel "Yn"
  set title "Metodo nuerico de Euler Inverso"
  set style line 1 pt 1
  set style line 2 pt 2
  set term png
  set output "graphs/eulerinverso.png"
  plot "output/eulerinverso.csv" u 1:2 pt 1 title "Euler_Inverso" w linespoints
EOF

gnuplot <<- EOF
  set grid layerdefault linewidth 1
  set xlabel "Passo"
  set ylabel "Yn"
  set title "Metodo de numerico de Euler Aprimorado"
  set style line 1 pt 1
  set style line 2 pt 2
  set term png
  set output "graphs/euleraprimorado.png"
  plot "output/euleraprimorado.csv" u 1:2 pt 1 title "Euler_Aprimorado" w linespoints
EOF

gnuplot <<- EOF
  set grid layerdefault linewidth 1
  set xlabel "Passo"
  set ylabel "Yn"
  set title "Metodo numerico de Runge Kutta"
  set style line 1 pt 1
  set style line 2 pt 2
  set term png
  set output "graphs/rungekutta.png"
  plot "output/rungekutta.csv" u 1:2 pt 1 title "Runge_Kutta" w linespoints
EOF

# gnuplot <<- EOF
#   set grid layerdefault linewidth 1
#   set xlabel "Passo"
#   set ylabel "Yn"
#   set title "Metodo numerico de Euler"
#   set style line 1 pt 1
#   set style line 2 pt 2
#   set term png
#   set output "graphs/euler.png"
#   plot "output/euler.csv" u 1:2 pt 1 title "Euler" w linespoints
# EOF

#, "output/slots.csv" u 1:3 title "Eom Lee" w linespoints