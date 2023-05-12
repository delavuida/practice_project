var products = 
[
    {
        name: "농구공",
        description : "평범한 농구공",
        price : 40000,
        seller : "민수"
    },
    {
        name: "축구공",
        description : "평범한 축구공",
        price : 60000,
        seller: "철수"
    }
]

/* 인자로 배열을 받았을 떄 길이를 return 하는 함수를 만드시오. 
   그리고 products를 넣어 실행하시오. */
function getProductsLength(array){
    return array.length;
}
getProductsLength(products)

var length = getProductsLength(products)
