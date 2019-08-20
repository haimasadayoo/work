# coding: utf-8
class Item
  def initialize(name, price)
    @name = name
    @price = price
  end
  # attr_reader は変数に対応するメソッドを作成し外部からの参照を
  # 可能にする
  # ちなみに attr_writer は代入を可能にする
  attr_reader :name, :price
end
class Items
  def initialize
    @items = []
  end
  def add(item)
    # class メソッドはそのオブジェクトのクラスを返す
    if item.class == Item
      # 配列の<<メソッドは引数を要素として追加する
      @items << item
    end
  end
  def each_name
    @items.each do |i|
      yield(i.name)
    end
  end
end
items = Items.new
items.add(Item.new("ディスプレイ", 79000))
items.add(Item.new("マウス", 3900))
items.add(Item.new("キーボード", 5800))
items.each_name do |name|
  puts name
end
