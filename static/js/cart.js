let updateButtons = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateButtons.length; i++)
{
    updateButtons[i].addEventListener("click", function() {
        let productId = this.dataset.product;
        let action = this.dataset.action;
        console.log({"id": productId, "action": action});
        
        if (user === "AnonymousUser") {console.log("User not loggedIn");}
        else {console.log(`User logged in as ${user}`);}
    })
}