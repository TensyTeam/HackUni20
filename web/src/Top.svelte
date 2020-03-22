<script>
	import api from './api';

	// Получение книг

	let books = [];

	function getTop(data={}) {
		const handlerSuccess = (res) => {
			books = res;
		};
		api('top', data, handlerSuccess);
	};

	getTop();
</script>

<div class="top">
	<div class="container">
		{#each books.slice(0) as book, i}
			<div class="book">
				<div class="book_img">
					<img src={book.img} alt={book.name}>
				</div>
				<div class="book_name">{book.name}</div>
			</div>
		{/each}
	</div>
</div>

<style>
	.top {
		width: 100%;
		margin-top: 50px;

		opacity: 0;
		animation: display 1s 1;
		animation-fill-mode: forwards;

		z-index: 1000;
    	position: relative;
	}

	@keyframes display {
		100% {
			opacity: 1;
		}
	}

	.container {
		width: 80vw;
		min-width: 250px;
		/* max-width: 550px; */

		margin-left: calc(10vw);

		display: flex;
	    align-items: center;
    	position: relative;
		overflow: scroll;
	}

	@media all and (min-width: 1000px) {
		.container {
			width: 800px;
			margin-left: calc(50vw - 400px);
		}
	}

	.book {
	    margin: 10px;
		text-align: center;
	}

	.book_name {
		font-size: 14px;
		height: 51px;

		/* Только 3 строки названия */

		overflow: hidden;
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
	}

	.book_img img {
		width: 100px;
		height: 150px;
	}
</style>
