var answers = $$('.rightAns');
corrects = []
for(answer of answers){
    corrects.push(answer.textContent.slice(0,-2))
}

chosens = []
var menus = $$('.menu-tbl');
for(tbl of menus){
    chosens.push(tbl.innerText.slice(-1));
}
let ans = 0;
for(let i=0;i<200;i++){
    if(corrects[i] === chosens[i]){
        ans+=1;
    }
}
console.log(ans);
