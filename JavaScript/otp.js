/* Implement a function that generates one - time alphanumerical 
                password, which is 12 characters long*/

const generateOTP = (length = 12) => {
    let otp = '';
    const characters = '0123456789{}[]!@#$%^&()"№;%:?|ABCDEFGHIJKLMOPQRSTUVWXYZ_*+/';
    for (let i = 0; i < length; i++) {
        const index = Math.floor(Math.random() * characters.length)
        otp += characters[index]
    }
    console.log(otp);
}

generateOTP()