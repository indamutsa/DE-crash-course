{% macro classify_ratings(colum_name) %}
    CASE
        WHEN {{ colum_name }} >= 4.5 THEN 'Excellent'
        WHEN {{ colum_name }} >= 4.0 THEN 'Good'
        WHEN {{ colum_name }} >= 3.0 THEN 'Average'
        ELSE 'Poor'
    END
{% endmacro %}