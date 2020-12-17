window.post_submit_value = 0;

function test_function(){
    console.log('test_function');
    return false;
}


function SaveandAddAnother(value){
    form = document.forms['create-post'];
    $.post('/create-post/',
    {
        csrfmiddlewaretoken: form.csrfmiddlewaretoken.value,
        title: form.title.value,
        author: form.author.value,
        short_description: form['short_description'].value,
        description: form.description.value,
    },
    function(data, status){
    form.innerHTML=data
    if (post_submit_value != 1){
        location = '/';
    }
    });
    return false;
}

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
            document.getElementById("LoginModal").innerHTML = data;
        }
    });
return false
}


$("#signup_button").click(function(){
    $.get("/user/create/",function(data,status){
        $("#SignUpModal")[0].innerHTML = data;
    });
});

function signup_form_submit(){
    form = document.forms["signup-form"];
    $.post("/user/create/",
    {
        csrfmiddlewaretoken: form.csrfmiddlewaretoken.value,
        username: form.username.value,
        email:form.email.value,
        password1: form.password1.value,
        password2: form.password2.value,
    },
    function(data,status){
        console.log(data)
        if(data=="1"){
            location = '/';
        }
        else{
            $("#SignUpModal")[0].innerHTML = data;
        }

    });
}


function load_login_form(){
    $.get('/user/login/',function(data,status){
        $("#LoginModal")[0].innerHTML = data;
    });
}


function load_add_post_form(){
    $.get('/create-post/',function(data,status){
        $("#AddPostModal")[0].innerHTML=data;
        window.post_creation_form = document.forms['create-post'];
    });
}

function set_post_submit_value(value){
    window.post_submit_value=value;
}
