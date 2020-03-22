<script>
	import api from './api';

	// Получение книг

	let books = [];

	getTop();
	function getTop(data={}) {
		const handlerSuccess = (res) => {
			books = res;
		};
		api('top', data, handlerSuccess);
	};
</script>

<div class="top">
	{#each books.slice(0) as book, i}
		<div class="book">
			<div class="book_img">
				<img src={book.img} alt={book.name}>
			</div>
			<div class="book_name">{book.name}</div>
		</div>
	{/each}
</div>

<style>
	.top {
		display: flex;
	    align-items: center;
		z-index: 1000;
    	position: relative;
    	overflow: scroll;
	}

	.book {
	    margin: 10px;
		text-align: center;
		background
	}

	.book_name {
		font-size: 14px;
	}

	.book_img  img {
		width: 150px;
		height: 250px;
	}
</style>
