/* Implement a fucntion that generates a one time password 
    comprised of digits, which is six characters long */ 
    function generateOTP() {
    var digits = '0123456789';
    let OTP = ' ';
    for (let i = 0; i < 6; i++) {
        OTP += digits[Math.floor(Math.random() * 10)];
    }
    console.log(OTP);
}

generateOTP()