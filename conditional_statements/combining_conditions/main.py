# The item's discount and stock status have been defined
discounted = False
lowStock = True

movingProduct = lowStock or discounted
promotion = not lowStock and not discounted
print (f"Is the item eligible for promotion? {promotion}")