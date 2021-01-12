import requests
def calc(i):
    return f'https://lecturenotes.in/material/v2/85/page-{i}?noOfItems=10'      # CHANGE
data = []
totalPages = 231        # CHANGE
for i in range(1,totalPages,10):
    res = requests.get(calc(i))
    data.extend(res.json()['page'])
for row in data:
    img_url = 'https://lecturenotes.in'+row['path']
    r = requests.get(img_url)
    title = 'page'
    pageNum = str(row['pageNum'])
    pageNum = '0'*(4-len(pageNum))+pageNum
    title += pageNum
    title += '.jpg'
    with open(title,'wb') as f:
        f.write(r.content)
        
# convert "*.{jpg}" -quality 100 {name}.pdf
