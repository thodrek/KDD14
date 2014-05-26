set ter postscript enhanced color eps "Helvetica" 30
set output "topic_dengue_timeline.eps"
set size ratio 0.4
set boxwidth 0.75 relative
set style fill solid 1.00 border lt -1
set style data histogram
set title "{/Helvetica-Bold Dengue"
set xlabel  "Week Index"
set ylabel  "Prominence"
set datafile missing "-"
set xrange[31:95]
set yrange[0.04:0.18]
set ytics (0.04, 0.08, 0.12, 0.16)
set xtic rotate by 90 font ",30"
set xtics offset 0,-3
set xtics ("01/13" 31, "02/13" 35, "03/13" 39, "04/13" 44, "05/13" 48, "06/13" 52, "07/13" 57, "08/13" 61, "09/13" 65, "10/13" 70, "11/13" 74, "12/13" 78, "01/14" 83, "02/14" 87, "03/14" 91)
set key off

plot "topic_dengue_timeline.dat" using 2
