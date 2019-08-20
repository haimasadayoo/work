
hoge = [3, 1, 2].sort()
p hoge
hoge = [3, 1, 2].sort() do |x, y|
  y <=> x
end
p hoge
