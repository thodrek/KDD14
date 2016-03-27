set ter postscript enhanced color eps "Helvetica" 25
set output "quality_bench.eps"
set size ratio 0.4
set boxwidth 0.75 relative
set title "{/Helvetica-Bold Quality Timeline"
set ylabel  "Quality Score"
set datafile missing "-"
set grid x y
set xrange[1:6]
set xtic rotate by 90 font ",25"
set xtics offset 0,-3
set xtics ("01/13" 1, "02/13" 2, "03/13" 3, "04/13" 4, "05/13" 5, "06/13" 6)
set key out horizontal center bottom
set autoscale y

plot "quality_bench.dat" using 1:2 with linespoints pt 7 ps 3 lw 4 lt 1 lc rgb "red" title "SingleSource", \
     "quality_bench.dat" using 1:3 with linespoints pt 14 ps 3 lw 4 lt 1 lc rgb "blue" title "SourceSeer"
