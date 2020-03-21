<script>
	import Search from './Search.svelte';

	let status = 0;
	let text = '';
</script>

<main>
	<Search
		bind:status={status}
		bind:text={text}
	/>
</main>