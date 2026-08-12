const p = new promise(funtion(reject, resolve){
    let promiseReady=true;
    if(promiseReady) {
        resolve("Done");
    }else{
        reject("Nope");
    }
});