const e = React.createElement;

// Display a "Like" <button>
const LikeButton = () => {
    return e(
        'button', { onClick: () => alert('Button was Clicked') },
        'Like'
    );
}

// const Button = () => {
//     return <button > like < /button>
// }
const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);