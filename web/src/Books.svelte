<script>
	import api from './api';

	export let text;
	let books=[];

	function getPosts(data={}) {
		const handlerSuccess = (res) => {
			books=res;
		};

		api('search', data, handlerSuccess);
	};

	getPosts({cont: text});
</script>

<div class="books">
	{#each books as book, i}
		<div class="book">
			<div>{i+1}.</div>
			<div>{book.name}</div>
		</div>
		<br />
	{/each}
</div>

<style>
	.books {
		width: 100%;

		text-align: center;
	}

	.book {
		width: 80vw;
		min-width: 250px;
		max-width: 550px;

		padding: 5px 0 5px 35px;

		text-align: left;
		font-size: 1.5rem;
	}

	.book div:first-child {
		width: 20px;
	}
</style>