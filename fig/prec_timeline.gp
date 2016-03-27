set ter postscript enhanced color eps "Helvetica" 25
set output "prec_timeline.eps"
set size ratio 0.4
set boxwidth 0.75 relative
set title "{/Helvetica-Bold Precision Timeline"
set ylabel  "Precision"
set datafile missing "-"
set grid x y
set xrange[1:15]
set xtic rotate by 90 font ",25"
set xtics offset 0,-3
set xtics ("01/13" 1, "02/13" 2, "03/13" 3, "04/13" 4, "05/13" 5, "06/13" 6, "07/13" 7, "08/13" 8, "09/13" 9, "10/13" 10, "11/13" 11, "12/13" 12, "01/14" 13, "02/14" 14, "03/14" 15)
set key out horizontal center bottom
set autoscale y

plot "prec_timeline.dat" using 1:2 with linespoints pt 6 ps 3 lw 4 lt 1 lc rgb "red" title "BSR", \
     "prec_timeline.dat" using 1:3 with linespoints pt 7 ps 3 lw 4 lt 1 lc rgb "green" title "KeyWord", \
     "prec_timeline.dat" using 1:4 with linespoints pt 3 ps 3 lw 4 lt 1 lc rgb "black" title "LocSeer", \
     "prec_timeline.dat" using 1:5 with linespoints pt 14 ps 3 lw 4 lt 1 lc rgb "blue" title "SourceSeer"
