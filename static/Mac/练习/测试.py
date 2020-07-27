import re
a=''''<link rel="dns-prefetch" href="//static.360buyimg.com"/> <link rel="dns-prefetch" href="//misc.360buyimg.com"/> <link rel="dns-prefetch" href="//img10.360buyimg.com"/> <link rel="dns-prefetch" href="//img11.360buyimg.com"/> <link rel="dns-prefetch" href="//img12.360buyimg.com"/> <link rel="dns-prefetch" href="//img13.360buyimg.com"/> <link rel="dns-prefetch" href="//img14.360buyimg.com"/> <link rel="dns-prefetch" href="//img20.360buyimg.com"/>'''
s='href="(//.*?img.*?)"/'
m=re.findall(s,a)
m.isalpha
print(m)