function my_function(){alert('lol');}
$('#SaveandAdd').click(function(){
form = document.forms['create-post'];
    $.post('/posts/',
    {
        csrfmiddlewaretoken: form.csrfmiddlewaretoken.value,
        title: form.title.value,
        author: form.author.value,
        short_description: form['short_description'].value,
        description: form.description.value,
    },
    function(data, status){
    form.innerHTML=da
    console.log(data);
    });
});


function my_submit(){
        console.log('login');
    form = document.forms["login_form"];
    $.post('/user/login/',
    {
        csrfmiddlewaretoken: form.csrfmiddlewaretoken.value,
        username:form.username.value,
        password:form.password.value,
    },
    function(data,status){
        if (data == 'true'){
            location.reload();
        }
        else{
            console.log(data);
            document.getElementById("LoginModal").innerHTML = data;
        }
    });

};
$("#signup_button").click(function(){
    $.get("/user/create/",function(data,status){
        $("#SignUpModal")[0].innerHTML = data;
    });
});

$("#signup_submit_button").click(function(){
console.log('hey user');
/**
    console.log("I'm Bangladesh");
    form = document.forms["signup-form"];
    $.post("/user/create/",
    {
        csrfmiddlewaretoken: form.middlewaretoken.value,
        username: form.username.value,
        password1: form.password1.value,
        password2: form.password2.value,
    },
    function(data,status){

    });
    */
});
