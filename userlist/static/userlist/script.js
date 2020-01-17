
function showit(id){
    elem = document.getElementsByClassName(id);
    console.log(id);
    console.log(elem);
    elem[0].style.display='inline-block';
}

function hideit(id){
    elem = document.getElementsByClassName(id);
    console.log(id);
    console.log(elem);
    elem[0].style.display='none';
}