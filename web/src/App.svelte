<script>
	import Search from './Search.svelte';
	import Books from './Books.svelte';
	import Filters from './Filters.svelte';

	let status = 0;
	let text = '';

	// Генерация токена

	function genereteToken() {
		const res = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
		return res.substr(0, 32);
	}

	let token = localStorage.getItem('token')

	if (token === null) {
		token = genereteToken()
		localStorage.setItem('token', token)
	}
</script>

<main>
	<Search
		bind:status={status}
		bind:text={text}
	/>
	<Books
		text={text}
	/>
	<Filters
		status={status}
	/>
</main>