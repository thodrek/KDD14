set ter postscript enhanced color eps "Helvetica" 22
set output "country_topic.eps"
set size square
set style fill pattern 1 border -1
set style data histogram
set style histogram cluster gap 1
set key out vertical right center 
set title "{/Helvetica-Bold Topic Prominence per Country"
set ylabel  "Prominence"
set xlabel "Topic"
set datafile missing "-"
set xtic rotate font ",22" out

plot for [COL=2:5] "country_topic.dat" using COL:xticlabels(1) title columnheader
