## LLM first create empty brower
```
driver = create_driver()
```
## 1st subtask: goto HKTV Mall
```
url = "https://www.hktvmall.com/hktv/zh/"
goto_url(url)
```
## 2nd subtask: search products with given test and scrap the prodcut data

search_products(text= 'protein')

## 3nd substaks

```
product_data = scrap_products()
```
## 4rd subtask: LLM to read the scrap data and return the selected product_code based on name/price/packing or even user preference

```
select_product_id = product_data[0]['product_code']
print(product_data[0])
```

Product_data.json

    {"product_code": "H0888001_S_10159916", "product_name": "VITAL PROTEINS - 膠原蛋白多肽","product_price": "$ 301.00", "packing_spec": "567克"}...



## 5th subtask: add the selected product to cart

Pass selected product id to tools
```
add_item_to_cart(select_product_id)
```

## Go to check out page

```
click_btn(driver, btn_class_name= "btn-cart")
```