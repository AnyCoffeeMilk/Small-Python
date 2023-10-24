def FunSq(n):
	t = n * 2 - 1
	if (t == 1):
		print(1)
		return 1
	o = []
	def ans(m):
		ans = ""
		for p in m:
			ans += str(p)
		print(ans)

	for i in range(t):
		o.append(1)
	
	ans(o)

	def Sth(a, c=0, e=[]):
		if c > t / 2 - 1:
			for a in e:
				ans(a)
			return a
		b = []
		d = c + 1
		for j, i in enumerate(a):
			if j <= d - 1 or j >= len(a) - d:
				b.append(i)
			else:
				i += 1
				b.append(i)
		ans(b)
		if (len(e) < t / 2 - 1.5):
			e.insert(0, b)
		return Sth(b, d, e)
	Sth(o)
	ans(o)

for n in range(9):
	FunSq(n+1)