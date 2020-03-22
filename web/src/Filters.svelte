<script>
	import { onMount } from 'svelte';

	export let status, text;

	let smiles = [{
		emoji: '😂',
		text: '',
		selected: false,
	}, {
		emoji: '♥️',
		text: '',
		selected: false,
	}, {
		emoji: '🤔',
		text: '',
		selected: false,
	}, {
		emoji: '🔥',
		text: '',
		selected: false,
	}, {
		emoji: '🕵️',
		text: '',
		selected: false,
	}, {
		emoji: '😳',
		text: '',
		selected: false,
	}, {
		emoji: '😭',
		text: '',
		selected: false,
	}, {
		emoji: '👽',
		text: '',
		selected: false,
	}, {
		emoji: '😱',
		text: '',
		selected: false,
	}, {
		emoji: '🤘',
		text: '',
		selected: false,
	}, {
		emoji: '🤯',
		text: '',
		selected: false,
	}, {
		emoji: '👩‍🎓',
		text: '',
		selected: false,
	}];

	// Определение размера смайликов

	function changeSize() {
		let smiles = document.querySelectorAll('.smile');
		smiles.forEach(smile => {
			let width = smile.clientWidth - 50;
			smile.setAttribute('style', `line-height: ${width}px; font-size: ${width}px;`);
		})
	}

	onMount(changeSize);

	window.onresize = changeSize;

	// Выбор фильтров

	function changeFilter(emoji) {
		let ind = text.indexOf(emoji);

		if (ind !== -1) {
			text = text.substring(0, ind) + text.substring(ind+3, text.length);

			if (text === " ") {
				text = "";
			}
		} else {
			text += emoji + " ";
		}

		smiles = smiles.map((el) => {
			if (el.emoji === emoji) {
				el.selected = ind === -1;
			}
			return el;
		})
	}
</script>

<div class={status === 0 ? 'filters' : status === 2 ? 'filters filters-back' : 'filters filters-extra'}>
	<div class="smiles">
		{#each smiles as smile, i}
			<div
				class={"smile" + (i>9 ? " extra5" : "") + (i>8 ? " extra3" : "") + (smile.selected ? " selected" : "")}
				id="button"
				on:click={() => {changeFilter(smile.emoji)}}
			>{smile.emoji}</div>
		{/each}
	</div>
</div>

<style>
	.filters {
		width: 100%;

		position: fixed;
		top: 47vh;

		display: block;

		text-align: center;

		background-color: #fff;
	}

	.filters-extra {
		animation: display 1s 1;
		animation-fill-mode: forwards;
	}

	.filters-back {
		/* 50vh - 25px
		-47vh
		3vh + 50px + 25px */
		top: calc(75px + 3vh); /*100px;*/
		animation: display-back 1s 1;
		animation-fill-mode: forwards;
	}

	@keyframes display {
		100% {
			top: calc(75px + 3vh);
		}
	}

	@keyframes display-back {
		100% {
			top: 47vh;
		}
	}

	.smiles {
		width: calc(80vw + 2 * 8px);
		min-width: calc(250px + 2 * 8px);
		max-width: calc(550px + 2 * 8px);
	}

	.smile {
		box-sizing: border-box; /* padding-box; */
		position: relative;
		width: calc(16.66% - 16px);
		padding: 25px 26px 25px 24px;
		background-color: #ffeaa7; /* rgba(0, 0, 0, 0.12); */
		border-radius: 15px;
		margin: 8px;
		cursor: pointer;

		overflow: hidden;
	}

	.selected {
		background-color: #fdcb6e; /* rgba(0, 0, 0, 0.3); */
	}

	.extra5 {
		display: inline-block;
	}

	.extra3 {
		display: inline-block;
	}

	@media all and (max-width: 590px) {
		.smile {
			width: calc(20% - 16px);
		}

		.extra5 {
			display: none;
		}
	}

	@media all and (max-width: 490px) {
		.smile {
			width: calc(25% - 16px);
		}

		.extra5 {
			display: inline-block;
		}
	}

	@media all and (max-width: 410px) {
		.smile {
			width: calc(33.33% - 16px);
		}

		.extra3 {
			display: none;
		}
	}

	.smile:before {
		content: "";
		padding-top: 100%;
		float: left;
	}
</style>