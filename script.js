// Variables
const name = "World";
let count = 0;
var message = "Hello";

// Function
function greet(userName) {
    return `Hello, ${userName}!`;
}

// Array
const numbers = [1, 2, 3, 4, 5];

// Object
const person = {
    name: "John",
    age: 30,
    greet() {
        console.log(`Hi, I'm ${this.name}`);
    }
};

// Loop
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

// Conditional
if (count === 0) {
    console.log("Count is zero");
} else {
    console.log("Count is not zero");
}

// Call function
console.log(greet(name));
person.greet();