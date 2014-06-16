set ter postscript enhanced color eps "Helvetica" 25
set output "hanta_timelines_Chile.eps"
set size ratio 0.4
set boxwidth 0.75 relative
set title "{/Helvetica-Bold Mentions of Hanta Keywords over Time"
set xlabel  "Date"
set ylabel  "# of Mentions"
set datafile missing "-"
set grid x y
set xrange[31:95]
set xtic rotate by 90 font ",25"
set xtics offset 0,-3
set xtics ("01/13" 31, "02/13" 35, "03/13" 39, "04/13" 44, "05/13" 48, "06/13" 52, "07/13" 57, "08/13" 61, "09/13" 65, "10/13" 70, "11/13" 74, "12/13" 78, "01/14" 83, "02/14" 87, "03/14" 91)
set key out horizontal center bottom
set autoscale y

plot "hanta_timelines.dat" using 1:2 with linespoints pt 6 ps 3 lw 4 lt 1 lc 1 title "Chile", \
     "hanta_timelines.dat" using 1:3 with linespoints pt 3 ps 3 lw 4 lt 1 lc 0 title "Argentina"