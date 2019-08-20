hash = {
  "k1" => "val1",
  "k2" => "val2",
  "k3" => "val3",
}

hash.each do |key, value|
  print "key = ", key, ", value = ", value, "\n"
end


print(hash["k1"],"\n")
print(hash.keys(),"\n")
print(hash.keys()[0],"\n")
print(hash[hash.keys()[1]],"\n")
