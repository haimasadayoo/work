hoge = "3, 1, 2"
p hoge

hoge=hoge.split(/, /)
p hoge

hoge=hoge.sort()
p hoge

hoge=hoge.join(", ")
p hoge

hoge = "3, 1, 2".split(/, /).sort().join(", ")
p hoge
