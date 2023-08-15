/**
 * File: 13-insert_number.c
 * Auth: Victorinox2
 */

#include "lists.h"

/*
 * insert_node - insert a number to sorted singly-linked-list
 * @ head: points the head of the linked list
 * @ The number to be inserted
 * Return: if the functions fails - NULL
 * otherwise - a pointer the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next-> < number)
		node = node->next;
	new->next = next;
	node->next = new;

	return (new);
}
