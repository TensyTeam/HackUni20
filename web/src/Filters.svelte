<script>
	import { onMount } from 'svelte';

	let smiles = [{
		emoji: '😄',
		text: '',
	}, {
		emoji: '♥️',
		text: '',
	}, {
		emoji: '😂',
		text: '',
	}, {
		emoji: '🤔',
		text: '',
	}, {
		emoji: '😔',
		text: '',
	}, {
		emoji: '🔥',
		text: '',
	}, {
		emoji: '😳',
		text: '',
	}, {
		emoji: '😭',
		text: '',
	}, {
		emoji: '😱',
		text: '',
	}, {
		emoji: '🤯',
		text: '',
	}, {
		emoji: '👽',
		text: '',
	}, {
		emoji: '🤘',
		text: '',
	}, {
		emoji: '🕵️',
		text: '',
	}, {
		emoji: '👩‍🎓',
		text: '',
	}];

	onMount(() => {
		let smiles = document.querySelectorAll('.smile');
		smiles.forEach(smile => {
			let width = smile.clientWidth - 50;
			smile.setAttribute('style', `line-height: ${width}px; font-size: ${width}px;`);
		})
	});
</script>

<div class="filters">
	<div class="smiles">
		{#each smiles as smile}
			<div class="smile" id="button">{smile.emoji}</div>
		{/each}
	</div>
</div>

<style>
	.filters {
		width: 100%;

		/* margin-top: 47vh; */

		text-align: center;
	}

	.smiles {
		width: calc(80vw + 2 * 8px);
		min-width: calc(250px + 2 * 8px);
		max-width: calc(550px + 2 * 8px);
	}

	.smile {
		box-sizing: border-box; /* padding-box; */
		position: relative;
		width: calc(20% - 16px);
		padding: 25px 26px 25px 24px;
		background-color: rgba(0, 0, 0, 0.12);
		border-radius: 15px;
		margin: 8px;

		overflow: hidden;
	}

	.smile:before {
		content: "";
		padding-top: 100%;
		float: left;
	}
</style>