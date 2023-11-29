#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: If memory allocation fails or head is NULL, returns NULL.
 *         Otherwise, returns the address of the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t)), *temp = *head;

	if (!new_node || !head)
		return (free(new_node), NULL);

	new_node->n = number;

	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
	return (*head = new_node);
	}

	while (temp->next && temp->next->n < number)
		temp = temp->next;

	new_node->next = temp->next;
	temp->next = new_node;

	return (new_node);
}

