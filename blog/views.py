{% extends 'blog/base.html' %}

{% block title %}Home | My Blog{% endblock %}

{% block content %}

<h1 class="mb-4">Latest Posts</h1>

{% if posts %}
    {% for post in posts %}
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h3 class="card-title">{{ post.title }}</h3>

                <p class="text-muted small">
                    Published on {{ post.created_at|date:"M d, Y" }}
                </p>

                <p class="card-text">
                    {{ post.content|truncatewords:25 }}
                </p>

                <a href="{% url 'blog:post_detail' post.slug %}" 
                   class="btn btn-primary">
                    Read more
                </a>
            </div>
        </div>
    {% endfor %}

    <!-- 🔽 Pagination -->
    <nav aria-label="Page navigation" class="mt-4">
        <ul class="pagination justify-content-center">

            {% if posts.has_previous %}
                <li class="page-item">
                    <a class="page-link"
                       href="?page=1{% if query %}&q={{ query }}{% endif %}">
                        First
                    </a>
                </li>

                <li class="page-item">
                    <a class="page-link"
                       href="?page={{ posts.previous_page_number }}{% if query %}&q={{ query }}{% endif %}">
                        Previous
                    </a>
                </li>
            {% endif %}

            <li class="page-item active">
                <span class="page-link">
                    Page {{ posts.number }} of {{ posts.paginator.num_pages }}
                </span>
            </li>

            {% if posts.has_next %}
                <li class="page-item">
                    <a class="page-link"
                       href="?page={{ posts.next_page_number }}{% if query %}&q={{ query }}{% endif %}">
                        Next
                    </a>
                </li>

                <li class="page-item">
                    <a class="page-link"
                       href="?page={{ posts.paginator.num_pages }}{% if query %}&q={{ query }}{% endif %}">
                        Last
                    </a>
                </li>
            {% endif %}

        </ul>
    </nav>

{% else %}
    <p class="text-muted">No posts available.</p>
{% endif %}

{% endblock %}
