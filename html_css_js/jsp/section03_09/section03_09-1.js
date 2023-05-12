function sayHello(){
    console.log("안녕하세요");
}

const sayHello2 = function()
{
    console.log("안녕하세요2");
}

sayHello();
sayHello2();

function calculate(x){
    var result = 3 * x + 5;
    console.log("결과 값은 " + result + " 입니다")
}
calculate(1);

calculate(10);

var getAge = function(name, age){
    console.log(name + "는 " + age + "살입니다." )
}

getAge('민수', 25);

// return은 값을 반할 수 있다. 여기서 값은 모든 자료형(string, number, 배열, 객체)
// 그리고 함수 또한 return이 가능

function calculate2(x) {
    var result = 2 * x + 3
    console.log(result);
    return result;
}

calculate2(1);

var result1 = calculate2(1);
var result2 = calculate2(2);

function getProfile(name, age){
    return {
        name : name,
        age : age
    }
}

getProfile("래리", 27);

var profile = getProfile("래리", 27);

console.log(profile.name);

// 함수에서 return을 실행하면 return 아래에 있는 코드는 실행되지 않는다.
// return은 함수를 종료시키는 구문이기도 하다

function sayHello3(){
    console.log("실행");
    return;
    console.log("실행 X");
}

sayHello3();

// 일반적으로 함수 안에 선언된 변수는 밖에서 사용이 불가능

function sayHi(){
    var name35 = "그랩";
}
// console.log(name35); name35 는 undefined

// 하지만 함수 밖에서 선언된 변수는 함수 {} 안에서 사용이 가능

var name36 = "민수"
function getName2(){
    console.log(name36);
}
getName2();

// {} 를 기준으로 밖에 있는 변수는 안에서도 사용이 가능
// if문에서도 {}가 사용되므로 마찬가지

if(true){
    console.log(name36);
}