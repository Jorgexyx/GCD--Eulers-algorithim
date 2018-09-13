'''
Project 1: Analysis of GCD
'''
import matplotlib.pyplot as plot
def EuclidAlgorithim(m,n): #computes the number of iterations to find gcd
	return 1 if (n == 0) else 1 + EuclidAlgorithim(n,m % n)

def consec_int_checking(m,n): #computes the number of iterations to find gcd
	t = m if (m < n) else n 
	cnt = 2
	while(t > 1):
		cnt += 2
		if(t % m is 0 & t % n is 0): break
		t -= 1
	return cnt

def fib_num(n): #computes the fibonnci sequence iteratively
	if( n <= 2):
		return 1
	a = 1
	b = 1
	c = 0
	for i in range(0,n-2):
		c = a + b
		b = a
		a = c
	return a

def setPlot(title,xlabel,ylabel):
	figure = plot.figure()
	plot.legend(loc='upper left')
	plot.title(title)
	plot.xlabel(xlabel)
	plot.ylabel(ylabel)
	return figure

def task_one_plot(n,md_avg,d_avg):
	figure = setPlot('average of operations x number','value','operations')
	ax1 = figure.add_subplot(111)
	ax1.scatter(n,md_avg, s = 10, c='b', marker="s", label='Eulers Algorithim')
	ax1.scatter(n,d_avg, s = 10, c='r', marker="o", label='Consecutive int checking')
	plot.show()

def task_two_plot(n,md_worse):
	figure = setPlot('# Modulo Divison x value','# modulo division','value')
	plot.scatter(n,md_worse, s = 10, c='b', marker="s", label='Eulers Algorithim')
	plot.show()

def main():
	n = []
	md_avg = []
	d_avg = []
	md_worse = []
	for i in range(50):
		n.append(i + 1)
	for j  in range(len(n)):
		val = n[j]
		e_avg = 0
		c_avg = 0
		e_worse = 0
		for i in range(val):
			e_avg += EuclidAlgorithim(val,i + 1)
			c_avg += consec_int_checking(val,i + 1)
			e_worse += EuclidAlgorithim(fib_num(val +1), fib_num(val))
		md_avg.append(e_avg / val)
		d_avg.append(c_avg / val)
		md_worse.append(e_worse / val)

	task_one_plot(n,md_avg,d_avg)
	task_two_plot(n,md_worse)

main()