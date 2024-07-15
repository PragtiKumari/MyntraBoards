function shareContent() {
    if (navigator.share) {
        navigator.share({
            title: 'Check out this Wishlist item!',
            text: 'Hey, take a look at this amazing item I found!',
            url: window.location.href,
        }).then(() => {
            console.log('Thanks for sharing!');
        }).catch((error) => {
            console.error('Something went wrong sharing the content:', error);
        });
    } else {
        alert('Web Share API is not supported in your browser.');
    }
}
