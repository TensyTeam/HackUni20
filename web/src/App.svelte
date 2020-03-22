<script>
	import Search from './Search.svelte';
	import Books from './Books.svelte';

	let status = 0;
	let text = '';
</script>

<main>
	<Search
		bind:status={status}
		bind:text={text}
	/>
	<Books
		text={text}
	/>
</main>