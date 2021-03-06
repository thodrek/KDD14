set ter postscript enhanced color eps "Helvetica" 30
set output "Argentina_1.eps"
set size ratio 0.4
set boxwidth 0.75 relative
set style fill solid 1.00 border lt -1
set style data histogram
set title "{/Helvetica-Bold Keyword mention timeline"
set xlabel  "Week Index"
set ylabel  "# of Mentions"
set datafile missing "-"
set xrange[31:95]
set yrange[0:180]
set ytics (0, 30, 60, 90, 120, 150, 180)
set xtic rotate by 90 font ",30"
set xtics offset 0,-3
set xtics ("01/13" 31, "02/13" 35, "03/13" 39, "04/13" 44, "05/13" 48, "06/13" 52, "07/13" 57, "08/13" 61, "09/13" 65, "10/13" 70, "11/13" 74, "12/13" 78, "01/14" 83, "02/14" 87, "03/14" 91)
set key off

plot "Argentina_1.txt" using 2
