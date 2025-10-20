# Django REST Framework Practice Projects 🛠️

This repository contains practice projects where I explore and implement various **Django REST Framework (DRF)** concepts. The main goal is to deepen my understanding of DRF and learn best practices for building robust APIs.

---

## 🔹 Key Concepts Covered

- **Serializers**  
  - Converting complex Django models into JSON and vice versa  
  - Nested serializers for related models

- **Mixins & Generic Views**  
  - Using `ListModelMixin`, `CreateModelMixin`, `RetrieveUpdateDestroyMixin`  
  - `GenericAPIView` and `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`

- **ViewSets & Routers**  
  - `ModelViewSet` for CRUD operations  
  - Automatic URL routing with `DefaultRouter`

- **Pagination**  
  - PageNumberPagination, LimitOffsetPagination, CursorPagination

- **Filtering, Searching & Ordering**  
  - Filter queryset by fields  
  - Search fields using `SearchFilter`  
  - Order results using `OrderingFilter`

- **Nested Relationships**  
  - Representing foreign key and many-to-many relationships in API responses

- **APIView & Function-Based Views (FBV)**  
  - Building APIs using `APIView` and `@api_view` decorators

---

## ⚡ Learning Goals

- Understand the difference between **FBV, CBV, Generic Views, and ViewSets**  
- Implement robust **CRUD APIs** using DRF best practices  
- Explore advanced DRF features like **pagination, filtering, ordering, and nested serializers**  
- Prepare for building **production-ready public APIs**

---

## 🗂️ Project Structure (Example)

```
Django_rest_main/
├── api/                # DRF views, serializers, and routers
├── student/            # Student app (FBV practice)
├── employes/           # Employee app (ViewSets & Mixins)
├── blog/               # Blog and Comment app (nested serializers, filtering)
├── Django_rest_main/   # Django project settings
```

---

💡 **Note:** This repository is purely for practice and learning purposes. It demonstrates different approaches to building DRF APIs, including function-based views, class-based views, viewsets, routers, and advanced DRF features like pagination, filtering, and ordering.